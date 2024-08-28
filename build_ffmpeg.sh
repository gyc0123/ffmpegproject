echo which
which cl
which link
which lib
echo "add cl to first of path"
cldir=$(dirname "$(which cl)")
echo $cldir
export PATH=$cldir:$PATH
echo $PATH
echo "which again"
which cl
which link
which lib

pacman -S make --noconfirm > /dev/null 
pacman -S diffutils --noconfirm > /dev/null 
mkdir -p /usr/local/bin
curl -o /usr/local/bin/yasm.exe http://www.tortall.net/projects/yasm/releases/yasm-1.3.0-win64.exe
yasm --version
which yasm
mkdir build
cd ffmpeg
echo configure
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc --prefix=../build
echo make
make -j4
make install

cd ..
ls .
ls ./FFmpeg
ls ./build

ls ./FFmpeg/libavformat
ls ./FFmpeg/libavcodec
ls ./FFmpeg/libavutil

