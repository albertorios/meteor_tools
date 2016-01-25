meteor create $1
rm $1/$1.*
mkdir $1/server $1/client $1/public $1/private
mkdir $1/client/lib
mkdir $1/client/lib/semantic
touch $1/client/lib/semantic/custom.semantic.json
cp setup.py $1/setup.py
cd $1
meteor add iron:router semantic:ui flemay:less-autoprefixer fourseven:scss okgrow:router-autoscroll
python setup.py
atom ./
meteor
