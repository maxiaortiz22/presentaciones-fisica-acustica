param(
    [Parameter(Mandatory = $true)][string]$DeckPath
)

$ErrorActionPreference = 'Stop'
$deck = [System.IO.Path]::GetFullPath($DeckPath)
$powerPoint = New-Object -ComObject PowerPoint.Application
$powerPoint.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $null
$darkSlides = @(1, 8, 18, 28, 40, 49, 61, 72, 82, 94, 105)

try {
    $presentation = $powerPoint.Presentations.Open(
        $deck,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse,
        [Microsoft.Office.Core.MsoTriState]::msoFalse
    )

    foreach ($slide in $presentation.Slides) {
        for ($i = $slide.Shapes.Count; $i -ge 1; $i--) {
            if ($slide.Shapes.Item($i).Name -eq 'auto-slide-number') {
                $slide.Shapes.Item($i).Delete()
            }
        }

        $number = $slide.Shapes.AddTextbox(1, 910, 515, 28, 16)
        $number.Name = 'auto-slide-number'
        $number.TextFrame.MarginLeft = 0
        $number.TextFrame.MarginRight = 0
        $number.TextFrame.MarginTop = 0
        $number.TextFrame.MarginBottom = 0
        $number.TextFrame.TextRange.InsertSlideNumber() | Out-Null
        $number.TextFrame.TextRange.ParagraphFormat.Alignment = 3
        $number.TextFrame.TextRange.Font.Name = 'Calibri'
        $number.TextFrame.TextRange.Font.Size = 10
        if ($darkSlides -contains $slide.SlideIndex) {
            $number.TextFrame.TextRange.Font.Color.RGB = 14540253
        }
        else {
            $number.TextFrame.TextRange.Font.Color.RGB = 8947848
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

[pscustomobject]@{
    deck = $deck
    slide_numbers = 'dynamic fields'
} | ConvertTo-Json
