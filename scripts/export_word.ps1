param([Parameter(Mandatory=$true)][string]$Source,[Parameter(Mandatory=$true)][string]$Target)
$ErrorActionPreference = 'Stop'
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
  $doc = $word.Documents.Open($Source, $false, $true)
  $doc.Repaginate()
  $doc.ExportAsFixedFormat($Target, 17)
  Write-Output ('Pages: ' + $doc.ComputeStatistics(2))
  $doc.Close(0)
} finally {
  $word.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
