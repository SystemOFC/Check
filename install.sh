url='https://github.com/SystemOFC/Check.git'
checkuser='https://github.com/SystemOFC/Check/raw/master/executable/checkuser'
depends=('git' 'python3' 'python3-pip' 'python3-setuptools' 'python3-dev')

cd ~

function install_dependencies() {
    for depend in ${depends[@]}; do
        echo 'Instalando ' $depend '...'
        sudo apt install $depend -y &>/dev/null
    done
}

function install_checkuser() {
    if [[ -d DTCheckUser ]]; then
        rm -rf DTCheckUser
    fi

    echo '[*] Clonando DTCheckUser...'
    git clone $url &>/dev/null
    cd DTCheckUser
    echo '[*] Instalando DTCheckUser...'
    pip3 install -r requirements.txt &>/dev/null
    sudo python3 setup.py install &>/dev/null
    cd ..
    rm -rf DTCheckUser
    echo '[+] DTCheckUser instalado!'
}

function start_checkuser() {
    echo '[*] Iniciando DTCheckUser...'
    read -p 'Porta: ' -e -i 5000 port
    checkuser --port $port --start --daemon

    addr=$(curl -s icanhazip.com)

    echo 'URL: http://'$addr':'$port''
    echo 'WS: ws://'$addr':'$port''
    read
}

function start_process_install() {
    install_dependencies
    install_checkuser
    start_checkuser
}

function uninstall_checkuser() {
    echo '[*] Parando DTCheckUser...'
    checkuser --stop &>/dev/null
    echo '[*] Desinstalando DTCheckUser...'
    python3 -m pip uninstall checkuser -y &>/dev/null
    rm -rf $(which checkuser)
    echo '[+] DTCheckUser desinstalado!'
    read
}

function reinstall_checkuser() {
    uninstall_checkuser
    install_checkuser
    start_checkuser
}

function is_installed() {
    return $(command -v checkuser &>/dev/null)
}

function get_version() {
    if is_installed; then
        echo $(checkuser --version | cut -d ' ' -f 2)
    else
        echo '-1'
    fi
}

function console_menu() {
    clear

    echo -n 'CHECKUSER MENU '
    if is_installed; then
        echo -e '\e[32m[INSTALADO]\e[0m - Versao:' $(get_version)
    else
        echo -e '\e[31m[DESINSTALADO]\e[0m'
    fi

    echo
    echo '[01] - INSTALAR CHECKUSER'
    echo '[02] - REINSTALAR CHECKUSER'
    echo '[03] - DESINSTALAR CHECKUSER'
    echo '[00] - SAIR'
    echo
    read -p 'Escolha uma opção: ' option

    case $option in
    01 | 1)
        start_process_install
        console_menu
        ;;
    02 | 2)
        reinstall_checkuser
        console_menu
        ;;
    03 | 3)
        uninstall_checkuser
        console_menu
        ;;
    00 | 0)
        echo '[*] Saindo...'
        exit 0
        ;;
    *)
        echo '[*] Opção inválida!'
        read -p 'Pressione ENTER para continuar...'
        console_menu
        ;;
    esac

}

function main() {
    case $1 in
    install | -i)
        start_process_install
        ;;
    reinstall | -r)
        reinstall_checkuser
        ;;
    uninstall | -u)
        uninstall_checkuser
        ;;
    *)
        echo "Usage: $0 [install | reinstall | uninstall]"
        exit 1
        ;;
    esac
}

if [[ $# -eq 0 ]]; then
    console_menu
else
    main $1
fi
