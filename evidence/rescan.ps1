$ErrorActionPreference = 'Stop'
$workspace = Split-Path $PSScriptRoot -Parent
Set-Location $workspace
$env:SCANCODE_CACHE = Join-Path $workspace '.work/scancode-cache'
$env:SCANCODE_TEMP = Join-Path $workspace '.work/scancode-temp'
$env:PYTHONUTF8 = '1'
$scan = Join-Path $workspace '.work/scancode-env/Scripts/scancode.exe'
if (-not (Test-Path $scan)) { throw 'Install ScanCode using the steps in README.md first.' }
& $scan --copyright --license --package --info --license-text --classify --summary --processes 2 --ignore .git --json-pp evidence/scancode-results.json --html evidence/scancode-results.html evidence/click-8.1.7 *> evidence/scan.log
exit $LASTEXITCODE
