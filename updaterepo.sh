repo-add vampirerepo.db.tar.gz *.zst
rm -rf *.old

git add .

git commit -m "fixing user@user error 1"

git push

sleep 10


echo "######################################################"
echo "                      done                             "
echo "######################################################"


notify-send "done"