openssl genpkey -algorithm RSA -out key.pem

rem Creating a Certificate Request (CSR)
openssl req -new -key key.pem -out csr.pem

rem Signing a certificate using a key (self-signed certificate)
openssl x509 -req -in csr.pem -signkey key.pem -out cert.pem