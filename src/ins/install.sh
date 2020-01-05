#!/bin/bash
clear
echo "
███████╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗██████╗     ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██╔════╝██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝╚════██╗    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
█████╗  ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝  █████╔╝    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██╔══╝  ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝   ╚═══██╗    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ██████╔╝    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ╚═════╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                
";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/fsociety3" ] ;
then
    echo "[◉] A directory fsociety3 was found! Do you want to replace it? [Y/n]:" ;
    read mama
    if [ $mama == "y" ];
    then
        rm -R "/usr/share/doc/fsociety3"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/CRO-THEHACKER/fsociety3.git /usr/share/doc/fsociety3;
echo "#!/bin/bash
python /usr/share/doc/fsociety3/src/platform/guess.py" '${1+"$@"}' > fsociety3;
chmod +x fsociety3;
sudo cp fsociety3 /usr/bin/;
rm fsociety3;


if [ -d "/usr/share/doc/fsociety3" ] ;
then
    echo "";
    echo "[✔] Tool istalled with success![✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔] ✔✔✔  All is done!! You can execute tool by typing fsociety3 !   ✔✔✔ [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation failed![✘] ";
    exit
fi
