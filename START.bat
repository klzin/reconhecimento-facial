@echo off
title Menu de Scripts
color 0A

:menu
cls
echo ========================================
echo          MENU DE SCRIPTS
echo ========================================
echo 1 - Extrair Caracteristicas
echo 2 - Buscar e Comparar Rostos
echo 0 - Sair
echo ========================================
set /p opcao="Escolha uma opcao: "

if "%opcao%"=="1" goto extrair_caracteristicas
if "%opcao%"=="2" goto buscar_rostos
if "%opcao%"=="0" goto sair

echo Opcao inválida! Tente novamente.
pause
goto menu

:extrair_caracteristicas
cls
echo Iniciando o script de extracao de características...
python processar_dados.py
pause
goto menu

:buscar_rostos
cls
echo Iniciando o script de busca e comparacao de rostos...
python comparar_rostos.py
pause
goto menu

:sair
cls
echo Saindo do programa. Até logo!
exit
