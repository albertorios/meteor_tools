if [[ $# -eq 0 ]] ; then
    echo 'Please enter a project name'
    exit 0
fi
meteor create $1
rm $1/$1.*
mkdir $1/server $1/client $1/public $1/private
mkdir $1/client/lib
mkdir $1/client/lib/semantic
touch $1/client/lib/semantic/custom.semantic.json
cd $1
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/setup.py
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/db.js
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/create_survey_db.py
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/create_survey_db.sh
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/db_template
wget https://raw.githubusercontent.com/albertorios/meteor_tools/master/owners
mv owners private/owners
mv db_template server/db_template
chmod 755 create_survey_db.sh
meteor add iron:router semantic:ui flemay:less-autoprefixer fourseven:scss  accounts-password accounts-ui okgrow:router-autoscroll session
meteor remove autopublish insecure
python setup.py
atom ./
meteor
