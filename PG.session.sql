SELECT *
FROM users
INNER JOIN users_info
ON users.cep = users_info.cep;
