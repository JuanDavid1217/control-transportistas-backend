DROP TABLE IF EXISTS "MetricasPorRuta";
DROP TABLE IF EXISTS "Rutas";
DROP TABLE IF EXISTS "Estatus";
DROP TABLE IF EXISTS "Unidades";
DROP TABLE IF EXISTS "Usuarios";

CREATE TABLE "Usuarios" (
	"id" BIGSERIAL PRIMARY KEY NOT NULL,
	"nombre" VARCHAR(100) NOT NULL,
	"email" VARCHAR(255) UNIQUE NOT NULL,
	"telefono" VARCHAR(10) NOT NULL,
	"fechaCreacion" TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

INSERT INTO "Usuarios"("nombre", "email", "telefono")
VALUES ('Juan Pérez', 'juan.perez@example.com', '1234567890');

INSERT INTO "Usuarios"("nombre", "email", "telefono")
VALUES ('María García', 'maria.garcia@example.com', '0987654321');

CREATE TABLE "Unidades" (
	"id" BIGSERIAL PRIMARY KEY NOT NULL,
	"placa" VARCHAR(15) UNIQUE NOT NULL,
	"marca" VARCHAR(100) NOT NULL,
	"modelo" VARCHAR(100) NOT NULL,
	"anio" SMALLINT NOT NULL,
	"usuarioId" BIGINT NOT NULL,
	"fechaCreacion" TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT "fk_unidad_usuario"
		FOREIGN KEY ("usuarioId") REFERENCES "Usuarios"("id") ON DELETE CASCADE
);

INSERT INTO "Unidades"("placa", "marca", "modelo", "anio", "usuarioId")
VALUES ('ABC-123', 'Toyota', 'Corolla', 2020, 1);

INSERT INTO "Unidades"("placa", "marca", "modelo", "anio", "usuarioId")
VALUES ('XYZ-789', 'Honda', 'Civic', 2021, 2);

CREATE TABLE "Estatus" (
	"id" SMALLSERIAL PRIMARY KEY NOT NULL,
	"nombre" VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO "Estatus"("nombre") VALUES ('Asignada');
INSERT INTO "Estatus"("nombre") VALUES ('En ruta');
INSERT INTO "Estatus"("nombre") VALUES ('Completada');

CREATE TABLE "Rutas" (
	"id" BIGSERIAL PRIMARY KEY NOT NULL,
	"unidadId" BIGINT NOT NULL,
	"inicio" TEXT NOT NULL,
	"destino" TEXT NOT NULL,
	"estatusId" SMALLINT NOT NULL DEFAULT 1,
	"horaInicio" TIMESTAMP WITH TIME ZONE,
	"horaFin" TIMESTAMP WITH TIME ZONE,
	CONSTRAINT "fk_ruta_unidad"
		FOREIGN KEY ("unidadId") REFERENCES "Unidades"("id") ON DELETE CASCADE,
	CONSTRAINT "fk_ruta_estatus"
		FOREIGN KEY ("estatusId") REFERENCES "Estatus"("id")
);

CREATE TABLE "MetricasPorRuta" (
	"id" BIGINT PRIMARY KEY NOT NULL,
	"distancia" NUMERIC(10,2) NOT NULL,
	"combustible" NUMERIC(10,2) NOT NULL,
	CONSTRAINT "fk_metrica_ruta"
		FOREIGN KEY ("id") REFERENCES "Rutas"("id") ON DELETE CASCADE
);