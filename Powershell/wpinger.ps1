param(
    [string]$StartIP,
    [string]$EndIP
)

function Test_IPRange{
    param(
        [string]$startIP,
        [string]$endIP
    )

    $start = [System.Net.IPAddress]::Parse($startIP)
    $end = [System.Net.IPAddress]::Parse($endIP)

    $actual = $start

    while ($actual.Address -le $end.Address){
        $ipToPing = $actual.ToString()
        $result = Test-Connection -ComputerName $ipToPing -Count 1 2>$null

        if ($result.StatusCode -eq 0) {
            Write-Host "$ipToPing - Activo"
        } else {
            Write-Host "$ipToPing - Fail"
        }
        Write-Host "$actual"
        $ipA = [System.Net.IPAddress]::Parse($actual)
        $octetos = $ipA.GetAddressBytes()
        $octetos[3]+= 1
        $actual = [System.Net.IPAddress]::new($octetos)

        Write-Host "$actual"
    }
}

if ($startIP -and $endIP){
    Test_IPRange $startIP $endIP
} else{
    Write-Host "Uso: .\wpinger.ps1 -StartIP <IP Inicio> -EndIP <IP Fin>"
}