DROP TABLE IF EXISTS backend;
CREATE TABLE backend(
    id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    experiencia INTEGER(2) NOT NULL,
    node INTEGER(2) NOT NULL,
    bsql INTEGER(2) NOT NULL,
    postgsql INTEGER(2) NOT NULL,
    aws INTEGER(2) NOT NULL,
    js INTEGER(2) NOT NULL,
    ningles FLOAT(5) NOT NULL,
    visap INTEGER(1) NOT NULL,
    hofice INTEGER(1) NOT NULL,
    estudios INTEGER(1) NOT NULL,
    
);
 

.headers ON
SELECT * FROM backend;