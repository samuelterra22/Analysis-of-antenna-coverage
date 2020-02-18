# Microsoft Developer Studio Project File - Name="P563" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** NICHT BEARBEITEN **

# TARGTYPE "Win32 (x86) Console Application" 0x0103

CFG=P563 - Win32 Debug
!MESSAGE Dies ist kein gültiges Makefile. Zum Erstellen dieses Projekts mit NMAKE
!MESSAGE verwenden Sie den Befehl "Makefile exportieren" und führen Sie den Befehl
!MESSAGE 
!MESSAGE NMAKE /f "P563.mak".
!MESSAGE 
!MESSAGE Sie können beim Ausführen von NMAKE eine Konfiguration angeben
!MESSAGE durch Definieren des Makros CFG in der Befehlszeile. Zum Beispiel:
!MESSAGE 
!MESSAGE NMAKE /f "P563.mak" CFG="P563 - Win32 Debug"
!MESSAGE 
!MESSAGE Für die Konfiguration stehen zur Auswahl:
!MESSAGE 
!MESSAGE "P563 - Win32 Release" (basierend auf  "Win32 (x86) Console Application")
!MESSAGE "P563 - Win32 Debug" (basierend auf  "Win32 (x86) Console Application")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=xicl6.exe
RSC=rc.exe

!IF  "$(CFG)" == "P563 - Win32 Release"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /D "_MBCS" /YX /FD /c
# ADD CPP /nologo /W3 /GX /Ox /Ot /Op /I ".\include" /I "..\nsplib\include" /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /D "_MBCS" /YX /FD /c
# ADD BASE RSC /l 0x407 /d "NDEBUG"
# ADD RSC /l 0x407 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=xilink6.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /machine:I386
# ADD LINK32 kernel32.lib user32.lib gdi32.lib nsp.lib /nologo /subsystem:console /machine:I386 /libpath:"..\nsplib\lib"

!ELSEIF  "$(CFG)" == "P563 - Win32 Debug"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "Debug"
# PROP BASE Intermediate_Dir "Debug"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "Debug"
# PROP Intermediate_Dir "Debug"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_CONSOLE" /D "_MBCS" /YX /FD /GZ /c
# ADD CPP /nologo /W3 /Gm /GX /ZI /Od /I ".\include" /I "..\nsplib\include" /D "WIN32" /D "_DEBUG" /D "_CONSOLE" /D "_MBCS" /YX /FD /GZ /c
# ADD BASE RSC /l 0x407 /d "_DEBUG"
# ADD RSC /l 0x407 /d "_DEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=xilink6.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /debug /machine:I386 /pdbtype:sept
# ADD LINK32 kernel32.lib user32.lib gdi32.lib nsp.lib /nologo /subsystem:console /debug /machine:I386 /pdbtype:sept /libpath:"..\nsplib\lib"

!ENDIF 

# Begin Target

# Name "P563 - Win32 Release"
# Name "P563 - Win32 Debug"
# Begin Group "Quellcodedateien"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=.\source\back_noise.c
# End Source File
# Begin Source File

SOURCE=.\source\beeprob.c
# End Source File
# Begin Source File

SOURCE=.\source\dsp.c
# End Source File
# Begin Source File

SOURCE=.\source\Enhance.c
# End Source File
# Begin Source File

SOURCE=.\source\EvalQual.c
# End Source File
# Begin Source File

SOURCE=.\source\hosm.c
# End Source File
# Begin Source File

SOURCE=.\source\inter_detect.c
# End Source File
# Begin Source File

SOURCE=.\source\lpc.c
# End Source File
# Begin Source File

SOURCE=.\source\LpcAnalysis.c
# End Source File
# Begin Source File

SOURCE=.\source\mapping.c
# End Source File
# Begin Source File

SOURCE=.\source\module1.c
# End Source File
# Begin Source File

SOURCE=.\source\module2.c
# End Source File
# Begin Source File

SOURCE=.\source\module3.c
# End Source File
# Begin Source File

SOURCE=.\source\p563.c
# End Source File
# Begin Source File

SOURCE=.\source\pitch.c
# End Source File
# Begin Source File

SOURCE=.\source\Quant.c
# End Source File
# Begin Source File

SOURCE=.\source\SignalsPercept.c
# End Source File
# Begin Source File

SOURCE=.\source\SpeechLib.c
# End Source File
# Begin Source File

SOURCE=.\source\Statistics.c
# End Source File
# Begin Source File

SOURCE=.\source\tools.c
# End Source File
# Begin Source File

SOURCE=.\source\tools1.c
# End Source File
# Begin Source File

SOURCE=.\source\vector_lib.c
# End Source File
# End Group
# Begin Group "Header-Dateien"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# Begin Source File

SOURCE=.\include\back_noise.h
# End Source File
# Begin Source File

SOURCE=.\include\beeprob.h
# End Source File
# Begin Source File

SOURCE=.\include\defines.h
# End Source File
# Begin Source File

SOURCE=.\include\dsp.h
# End Source File
# Begin Source File

SOURCE=.\include\Enhance.h
# End Source File
# Begin Source File

SOURCE=.\include\EvalQual.h
# End Source File
# Begin Source File

SOURCE=.\include\generic_typedefs.h
# End Source File
# Begin Source File

SOURCE=.\include\hosm.h
# End Source File
# Begin Source File

SOURCE=.\include\interr_detect.h
# End Source File
# Begin Source File

SOURCE=.\include\lpc.h
# End Source File
# Begin Source File

SOURCE=.\include\LpcAnalysis.h
# End Source File
# Begin Source File

SOURCE=.\include\mapping.h
# End Source File
# Begin Source File

SOURCE=.\include\module1.h
# End Source File
# Begin Source File

SOURCE=.\include\module2.h
# End Source File
# Begin Source File

SOURCE=.\include\module3.h
# End Source File
# Begin Source File

SOURCE=.\include\pitch.h
# End Source File
# Begin Source File

SOURCE=.\include\Quant.h
# End Source File
# Begin Source File

SOURCE=.\include\QuantTab.h
# End Source File
# Begin Source File

SOURCE=.\include\resource.h
# End Source File
# Begin Source File

SOURCE=.\include\SignalsPercept.h
# End Source File
# Begin Source File

SOURCE=.\include\SpeechLib.h
# End Source File
# Begin Source File

SOURCE=.\include\Statistics.h
# End Source File
# Begin Source File

SOURCE=.\include\tools.h
# End Source File
# Begin Source File

SOURCE=.\include\tools1.h
# End Source File
# Begin Source File

SOURCE=.\include\vector_lib.h
# End Source File
# End Group
# Begin Group "Ressourcendateien"

# PROP Default_Filter "ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe"
# End Group
# End Target
# End Project
