x=$(find content  | grep post | sort | tail -n 1)
exec vim $x
