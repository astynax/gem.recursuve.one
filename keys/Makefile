cert.pem:
	openssl req -x509 -newkey rsa:4096 \
	-keyout key.rsa -out cert.pem \
	-days 3650 -nodes -subj "/CN=recursive.one" \
	&& chmod a+r key.rsa cert.pem
