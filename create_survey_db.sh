if [[ $# -eq 0 ]] ; then
    echo 'Please enter a database name'
    exit 0
fi
mkdir server/$1
mkdir private/$1
cp server/db_template server/$1/$1_db.js
cp private/owners private/$1/owners.json
python create_survey_db.py $1
