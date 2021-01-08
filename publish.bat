if exist target (echo target folder already exits.) else (mkdir target)
powershell Compress-Archive -Force -LiteralPath "index.html" -DestinationPath target\sparkling_%1.zip
powershell Compress-Archive -Update -Path "./js" -DestinationPath target\sparkling_%1.zip"