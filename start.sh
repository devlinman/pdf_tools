#! /bin/bash


clean () {
    [ -d ./dist ] && rm -r ./dist
    [ -d ./build ] && rm -r ./build
    [ -d ./.venv ] && rm -r ./.venv
    [ -f *.spec ] && rm *.spec

}

if [ "$1" == "clean" ]; then
    clean
    exit
fi

python -m venv .venv
source ./.venv/bin/activate
pip install --upgrade pip
echo source ./.venv/bin/activate
echo source ./.venv/bin/activate | xsel -ib

pip install pymupdf

if [ "$2" == "bin" ]; then
    [ ! -f $1 ] && echo -e "\n\tNot A Valid File Path\n" && exit 100
    if [ "${1##*.}" != "py" ]; then
        echo -e "\n\tNot A Valid Python File\n" && exit 200
    fi
    pip install pyinstaller
    pyinstaller --onefile $1
    mv ./dist/* ./
    clean()
fi
