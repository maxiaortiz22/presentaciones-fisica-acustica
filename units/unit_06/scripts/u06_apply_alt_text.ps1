param(
    [Parameter(Mandatory = $true)][string]$DeckPath,
    [Parameter(Mandatory = $true)][string]$SlideTextPath
)

$ErrorActionPreference = 'Stop'
$deck = [System.IO.Path]::GetFullPath($DeckPath)
$source = [System.IO.Path]::GetFullPath($SlideTextPath)
$lines = Get-Content -LiteralPath $source -Encoding UTF8
$altByNumber = @{}
$current = $null
foreach ($line in $lines) {
    if ($line -match '^### U06-(\d{3})\b') { $current = [int]$Matches[1]; continue }
    if ($null -ne $current -and $line -match '^- \*\*Texto alternativo:\*\*\s*(.+)$') {
        $altByNumber[$current] = $Matches[1].Trim()
    }
}

$powerPoint = New-Object -ComObject PowerPoint.Application
$powerPoint.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $null
$updated = 0
try {
    $presentation = $powerPoint.Presentations.Open(
        $deck,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse
    )
    for ($i = 1; $i -le $presentation.Slides.Count; $i++) {
        $alt = $altByNumber[$i]
        if ([string]::IsNullOrWhiteSpace($alt)) { continue }
        $assignedDiagramSummary = $false
        $shapes = $presentation.Slides.Item($i).Shapes
        for ($j = 1; $j -le $shapes.Count; $j++) {
            $shape = $shapes.Item($j)
            $name = [string]$shape.Name
            $isPicture = ($shape.Type -eq 13 -or $shape.Type -eq 28)
            $isDiagramSummary = (-not $assignedDiagramSummary -and $name -match '^U06-DG-.+-box$')
            if ($isPicture -or $isDiagramSummary) {
                $shape.AlternativeText = $alt
                $shape.Title = ('Texto alternativo U06-{0:D3}' -f $i)
                $updated++
                if ($isDiagramSummary) { $assignedDiagramSummary = $true }
            }
        }
    }
    $presentation.Save()
}
finally {
    if ($null -ne $presentation) { $presentation.Close() }
    $powerPoint.Quit()
    if ($null -ne $presentation) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null }
    if ($null -ne $powerPoint) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

[pscustomobject]@{ deck = $deck; alt_text_assignments = $updated } | ConvertTo-Json
