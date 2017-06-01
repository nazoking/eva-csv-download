for i in $(seq 0 5)
do
  url=http://lovegundam.dtiblog.com/category7-$i.html
  out=raw/text-$i.txt
  w3m $url -dump -cols 1000 > $out
  echo "$url => $out"
done

