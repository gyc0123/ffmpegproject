##add cl to first of path
#cldir=$(dirname $(which cl))
#echo $cldir
#export PATH=cldir:$PATH
#echo $PATH


pacman -S make --noconfirm
pacman -S diffutils --noconfirm

build_dir=$(pwd)/build
cd ffmpeg
echo configure
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc -prefix=${build_dir}
echo make
make -j4

ls .
ls ./FFmpeg
ls ./build

ls ./FFmpeg/libavformat
ls ./FFmpeg/libavcodec
ls ./FFmpeg/libavutil
