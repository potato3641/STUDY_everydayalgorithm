@echo off.
cd ../..
git pull origin master
git add .
git commit -m 'batch_commiter'
git push origin master
timeout 4