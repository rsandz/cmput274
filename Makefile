commit:
	(git add --all && git commit -m "`date`" && git push origin master) || (echo "No new files added" && git push origin master)
