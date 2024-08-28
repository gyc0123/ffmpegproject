##add cl to first of path
#cldir=$(dirname $(which cl))
#echo $cldir
#export PATH=cldir:$PATH
#echo $PATH


pacman -S make --noconfirm > /dev/null 
pacman -S diffutils --noconfirm > /dev/null 
curl -o /usr/local/bin/yasm.exe http://www.tortall.net/projects/yasm/releases/yasm-1.3.0-win64.exe
build_dir=$(pwd)/build
cd ffmpeg
echo configure
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc --prefix=../build
echo make
make -j4

ls .
ls ./FFmpeg
ls ./build

ls ./FFmpeg/libavformat
ls ./FFmpeg/libavcodec
ls ./FFmpeg/libavutil
