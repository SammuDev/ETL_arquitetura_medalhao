SELECT
    users.id,
    users.nome,
    users.email,
    users.telefone,
    users_info.logradouro,
    users_info.estado,
    users_info.regiao
FROM users
INNER JOIN users_info
ON users.cep = users_info.cep;
