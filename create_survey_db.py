import sys
s_name=sys.argv[1]

f = open('db.js','r')
filedata = f.read()
f.close()

newdata = filedata.replace("//DATABASE",s_name.capitalize()+"_DB = new Mongo.Collection('"+s_name+"_db');\n//DATABASE")
newdata = newdata.replace("//SUBSCRIBE","Meteor.subscribe('"+s_name+"_db');\n  //SUBSCRIBE")

f = open('db.js','w')
f.write(newdata)
f.close()


f = open('server/'+s_name+'/'+s_name+'_db.js','r')
filedata = f.read()
f.close()

newdata = filedata.replace("SURVEYNAME",s_name.capitalize())
newdata = newdata.replace("surveyname",s_name)

f = open('server/'+s_name+'/'+s_name+'_db.js','w')
f.write(newdata)
f.close()
