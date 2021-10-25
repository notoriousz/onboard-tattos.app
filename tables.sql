CREATE TABLE public.tatuador
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    telefone character varying(25) NOT NULL,
    address character varying(255) NOT NULL,
    created_at date NOT NULL DEFAULT CURRENT_DATE,
    update_at character varying(25),
    PRIMARY KEY (id)
);

CREATE TABLE public.portifolio
(
    id_tatuador integer NOT NULL,
    created_at date NOT NULL DEFAULT CURRENT_DATE,
    update_at date,
    images character varying(1000)
);

ALTER TABLE IF EXISTS public.tatuador and public.portifolio
    OWNER to postgres;
