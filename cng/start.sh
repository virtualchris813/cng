#echo "I_LEN is ${I_LEN}"
#echo "F_ORDER is ${F_ORDER}"
#echo "D_HOST is ${D_HOST}"
#echo "D_USER is ${D_USER}"
#echo "D_PASS is ${D_PASS}"
#echo "D_DB is ${D_DB}"
#echo "D_PORT is ${D_PORT}"

if [ -z "${I_LEN}" ] || [ -z "${F_ORDER}" ] || [ -z "${D_HOST}" ] || [ -z "${D_USER}" ] || [ -z "${D_PASS}" ] || [ -z "${D_DB}" ]; then
	echo "A required parameter is missing. The following is what I recieved."
	echo "I_LEN is ${I_LEN}"
	echo "F_ORDER is ${F_ORDER}"
	echo "D_HOST is ${D_HOST}"
	echo "D_USER is ${D_USER}"
	echo "D_PASS is ${D_PASS}"
	echo "D_DB is ${D_DB}"
	exit 1
fi

sed -i "s/I_LEN/${I_LEN}/g" /cng/cng_vars.py
sed -i "s/F_ORDER/${F_ORDER}/g" /cng/cng_vars.py
sed -i "s/D_HOST/${D_HOST}/g" /cng/cng_db.py
sed -i "s/D_USER/${D_USER}/g" /cng/cng_db.py
sed -i "s/D_PASS/${D_PASS}/g" /cng/cng_db.py
sed -i "s/D_DB/${D_DB}/g" /cng/cng_db.py

if [ -z "${I_LEN}" ]; then
	echo "DB Port not provided, using default of 5432"
	sed -i "s/D_PORT/5432/g" /cng/cng_db.py
else
	sed -i "s/D_PORT/${D_PORT}/g" /cng/cng_db.py
fi

echo "Config file prepared, starting application."
python /cng/app.py
