param(
  [Parameter(Mandatory = $true)][string]$PptxPath,
  [Parameter(Mandatory = $true)][string]$SlideTextPath
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$slideText = [System.IO.File]::ReadAllText((Resolve-Path $SlideTextPath), [System.Text.Encoding]::UTF8)
$altById = @{}
$blocks = [regex]::Split($slideText, '(?m)^## ')
foreach ($block in $blocks) {
  if ($block -notmatch '^(U07-\d{3})') { continue }
  $id = $Matches[1]
  $match = [regex]::Match($block, '(?ms)- \*\*Texto alternativo:\*\*\s*(.+?)(?=\r?\n\r?\n|\z)')
  if ($match.Success) {
    $altById[$id] = ($match.Groups[1].Value -replace '\s+', ' ').Trim()
  }
}

$resolvedPptx = (Resolve-Path $PptxPath).Path
$stream = [System.IO.File]::Open($resolvedPptx, [System.IO.FileMode]::Open, [System.IO.FileAccess]::ReadWrite, [System.IO.FileShare]::None)
$archive = [System.IO.Compression.ZipArchive]::new($stream, [System.IO.Compression.ZipArchiveMode]::Update, $false)
$updated = 0
try {
  for ($slideNumber = 1; $slideNumber -le 999; $slideNumber++) {
    $entryName = "ppt/slides/slide$slideNumber.xml"
    $entry = $archive.GetEntry($entryName)
    if ($null -eq $entry) { continue }
    $id = 'U07-{0:D3}' -f $slideNumber
    if (-not $altById.ContainsKey($id)) { continue }

    $reader = [System.IO.StreamReader]::new($entry.Open(), [System.Text.Encoding]::UTF8)
    try { $xml = $reader.ReadToEnd() } finally { $reader.Dispose() }
    $escapedAlt = [System.Security.SecurityElement]::Escape($altById[$id])
    $pattern = '(<p:cNvPr\s+id="\d+"\s+name="' + [regex]::Escape($id) + '-[^"]+")(?<tail>\s*/>)'
    $replacement = '${1} descr="' + $escapedAlt + '"${tail}'
    $newXml = [regex]::Replace($xml, $pattern, $replacement)
    if ($newXml -eq $xml) { continue }

    $entry.Delete()
    $newEntry = $archive.CreateEntry($entryName, [System.IO.Compression.CompressionLevel]::Optimal)
    $writer = [System.IO.StreamWriter]::new($newEntry.Open(), [System.Text.UTF8Encoding]::new($false))
    try { $writer.Write($newXml) } finally { $writer.Dispose() }
    $updated++
  }
} finally {
  $archive.Dispose()
  $stream.Dispose()
}

Write-Output "Alt text added to $updated slide image(s)."
if ($updated -eq 0) { throw 'No slide images received alt text.' }
