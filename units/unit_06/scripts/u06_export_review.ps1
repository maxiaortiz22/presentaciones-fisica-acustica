param(
    [Parameter(Mandatory = $true)][string]$DeckPath,
    [Parameter(Mandatory = $true)][string]$PdfPath,
    [Parameter(Mandatory = $true)][string]$RenderDir
)

$ErrorActionPreference = 'Stop'
$deck = [System.IO.Path]::GetFullPath($DeckPath)
$pdf = [System.IO.Path]::GetFullPath($PdfPath)
$render = [System.IO.Path]::GetFullPath($RenderDir)
New-Item -ItemType Directory -Force -Path $render | Out-Null

$powerPoint = New-Object -ComObject PowerPoint.Application
$powerPoint.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $null
try {
    $presentation = $powerPoint.Presentations.Open(
        $deck,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse
    )
    $presentation.SaveAs($pdf, 32)
    for ($i = 1; $i -le $presentation.Slides.Count; $i++) {
        $name = ('slide-{0:D3}.png' -f $i)
        $presentation.Slides.Item($i).Export((Join-Path $render $name), 'PNG', 1600, 900)
    }
}
finally {
    if ($null -ne $presentation) { $presentation.Close() }
    $powerPoint.Quit()
    if ($null -ne $presentation) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null }
    if ($null -ne $powerPoint) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

[pscustomobject]@{
    deck = $deck
    pdf = $pdf
    slides = (Get-ChildItem -LiteralPath $render -Filter '*.png').Count
} | ConvertTo-Json
