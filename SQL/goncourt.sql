START TRANSACTION;

DROP TABLE IF EXISTS
    `go_book_selection`,
    `go_main_character`,
    `go_selection`,
    `go_jury`,
    `go_book`,
    `go_author`,
    `go_publisher`;

CREATE TABLE IF NOT EXISTS `go_author` (
    `au_id_author` INT NOT NULL AUTO_INCREMENT,
    `au_first_name` VARCHAR(50) NOT NULL,
    `au_last_name` VARCHAR(50) NOT NULL,
    `au_biography` TEXT DEFAULT NULL,
    PRIMARY KEY (`au_id_author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_jury` (
   `ju_id_jury` INT NOT NULL AUTO_INCREMENT,
   `ju_first_name` VARCHAR(50) NOT NULL,
   `ju_last_name` VARCHAR(50) NOT NULL,
   `ju_joining_date` DATE NOT NULL,
   `ju_is_president` BOOLEAN NOT NULL,
   PRIMARY KEY (ju_id_jury)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_selection` (
    `se_id_selection` INT NOT NULL AUTO_INCREMENT,
    `se_number` INT NOT NULL,
    `se_date` DATE NOT NULL,
    PRIMARY KEY (`se_id_selection`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_publisher` (
    `pu_id_publisher` INT NOT NULL AUTO_INCREMENT,
    `pu_name` VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (`pu_id_publisher`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_book` (
    `bo_id_book` INT NOT NULL AUTO_INCREMENT,
    `bo_title` VARCHAR(100) NOT NULL,
    `bo_summary` TEXT DEFAULT NULL,
    `bo_publication_date` DATE DEFAULT NULL,
    `bo_number_of_pages` INT DEFAULT NULL,
    `bo_isbn` VARCHAR(20) DEFAULT NULL,
    `bo_price` DECIMAL(10,2) DEFAULT NULL,
    `bo_id_author` INT NOT NULL,
    `bo_id_publisher` INT NOT NULL,
    PRIMARY KEY (`bo_id_book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_main_character`(
   `mc_id_main_character` INT NOT NULL AUTO_INCREMENT,
   `mc_name` VARCHAR(50) NOT NULL,
   `mc_id_book` INT NOT NULL,
   PRIMARY KEY (mc_id_main_character)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

CREATE TABLE IF NOT EXISTS `go_book_selection` (
   bs_id_book INT NOT NULL,
   bs_id_selection INT NOT NULL,
   PRIMARY KEY (bs_id_book, bs_id_selection)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

ALTER TABLE `go_book`
    ADD CONSTRAINT `go_book_fk_1` FOREIGN KEY (`bo_id_author`) REFERENCES `go_author` (`au_id_author`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `go_book_fk_2` FOREIGN KEY (`bo_id_publisher`) REFERENCES `go_publisher` (`pu_id_publisher`)
    ON DELETE CASCADE;

ALTER TABLE `go_main_character`
    ADD CONSTRAINT `go_main_character_fk1` FOREIGN KEY (`mc_id_book`) REFERENCES `go_book` (`bo_id_book`)
    ON DELETE CASCADE;

ALTER TABLE `go_book_selection`
    ADD CONSTRAINT `go_book_selection_fk1` FOREIGN KEY (`bs_id_book`) REFERENCES `go_book` (`bo_id_book`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `go_book_selection_fk2` FOREIGN KEY (`bs_id_selection`) REFERENCES `go_selection` (`se_id_selection`)
    ON DELETE CASCADE;

INSERT INTO `go_author` (`au_first_name`, `au_last_name`) VALUES
    ("Philippe", "Jaenada"),
    ("Anne", "Godard"),
    ("Yannick", "Haenel"),
    ("Lilia", "Hassaine"),
    ("Sonia", "Devillers"),
    ("Louise", "Chennevière"),
    ("Olivier", "Rolin"),
    ("Ananda", "Devi"),
    ("Sylvain", "Prudhomme"),
    ("Clémentine", "Mélois"),
    ("Boris", "Bergmann"),
    ("Jean-Yves", "Jouannais"),
    ("Olivier", "Grondeau"),
    ("Emma", "Marsantes"),
    ("Patrice", "Trigano"),
    ("Thélyson", "Orélien");

INSERT INTO `go_jury`(`ju_first_name`, `ju_last_name`, `ju_joining_date`, `ju_is_president`) VALUES
    ("Didier", "Decoin", "1995-06-06", false),
    ("Françoise", "Chandernagor", "1995-06-06", false),
    ("Tahar", "Ben Jelloun", "2008-05-06", false),
    ("Paule", "Constant", "2013-01-08", false),
    ("Philippe", "Claudel", "2012-01-11", true),
    ("Pierre", "Assouline", "2012-01-11", false),
    ("Eric-Emmanuel", "Schmitt", "2016-01-05", false),
    ("Camille", "Laurens", "2020-02-11", false),
    ("Pascal", "Bruckner", "2020-02-11", false),
    ("Christine", "Angot", "2023-02-28", false);

INSERT INTO `go_selection` (`se_number`, `se_date`) VALUES
    (1, "2026-09-02"),
    (2, "2026-10-06"),
    (3, "2026-10-27");

INSERT INTO `go_publisher` (`pu_name`) VALUES
    ("Albin Michel"),
    ("POL"),
    ("Grasset"),
    ("R.Laffont"),
    ("Actes Sud"),
    ("l'Iconoclaste"),
    ("Gallimard"),
    ("Flammarion"),
    ("Verdier"),
    ("Minuit"),
    ("M.Nadeau");



INSERT INTO `go_book` (`bo_title`, `bo_id_author`, `bo_id_publisher`,`bo_summary`, `bo_publication_date`,
    `bo_number_of_pages`, `bo_isbn`, `bo_price`) VALUES

    ("Minotaure", 11, 1,
    "Être l'indésiré, né hors du désir du père, voilà mon acte de naissance. J'y réponds par un désir extrême, une surenchère d'histoires vécues... ou racontées. Après tout, le Minotaure est un Forçat du sentiment. Forcé d'aimer tous ceux qu'il rencontre. Avant de les dévorer. »",
    "2026-08-19", 242, "9782226511874", 20.9),

    ("Faire la peau", 6, 2,
    "Je dis que l'une des plus tenaces fictions tient tout entière dans ce mot, mère. Que la haine qui circule entre les mères et leurs filles est sauvage, et qu'il faut la regarder droit dans les yeux.",
    "2026-08-20", 286, "9782818063583", 21.0),

    ("Chronique d'un royaume perdu", 8, 3,
    "Au Bouchon, petit village isolé de l’île Maurice, quatre générations se succèdent depuis le temps de l’esclavage. La violence se mêle à l’amour, la tendresse à la haine, les plus nobles passions aux vices les plus vils, les sangs des unes aux sangs des autres…\nLes cinq fondateurs viennent d’une plantation lointaine  : trois sont nés dans la puissante et blanche famille Dumontais  ; deux d’une esclave noire. Mais les trois blancs sont en vérité le fruit d’une passion entre Madame et le Vieux Bouc, un esclave magnétique qui revendique aussi la paternité des deux derniers. Bannis pour s’être liés d’amour et d’amitié, les cinq enfants devenus grands trouvent refuge dans ce lieu perdu dont ils font leur royaume, autarcique et magique, qu’ils défendent d’un seul corps, puisqu’ici sont abolies les frontières entre passé, présent et avenir  ; vie et mort  ; réel et fantastique.\nTel homme entend sans le vouloir tous les péchés humains  ; telle femme meurt et renait en déesse protectrice  ; un enfant vit parmi les oiseaux quand son cousin viole et tue sans frein  ; le moulin est hanté par les voix des fantômes, la nature donne les plus beaux fruits mais décapite la chapelle  ; les guerres du monde contemporain rencontrent les combats intérieurs de chaque individu et l’histoire de l’humanité se reproduit dans l’infiniment petit de leurs existences débridées. Parmi eux, un enfant timide sera le chroniqueur de ce royaume hors-norme dont il livre les jours de paix, de luttes, et les nuits de folie pour empêcher l’oubli.\nÉpopée fabuleuse,  mythologie vibrante, fable majestueuse, cette Chronique d’un Royaume perdu est le chef d’œuvre d’Ananda Devi.",
    "2026-08-19", 454, "9782246846949", 24.0),

    ("Le fabuleux piano", 5, 4,
    "Après le succès littéraire et commercial de son récit Les Exportés , Sonia Devillers part à la recherche d'un admirable piano à queue, volé par les nazis en 1943. Ce qu'elle nous raconte est bouleversant, instructif, et magistralement mené.\nLe fabuleux piano est un instrument volé par les Allemands, en 1943, à des juifs qui le cherchent encore... Dans ce vide impossible à combler, Sonia Devillers entend une résonance intime, le souvenir d'un instrument que sa propre grand-mère, forcée à l'exil, a regretté toute sa vie. Elle part alors sur les traces des pianos fantômes pillés par milliers sous l'Occupation et transportés jusqu'aux confins du IIIe Reich.\nAvec cet instrument de concert ressurgit l'incroyable destin d'une famille d'éditeurs de musique, les Enoch. Un siècle de partitions, des menuets de Ravel aux ritournelles de Prévert. Les nazis se sont acharnés sur les Enoch, mais ils ont échoué à les réduire au silence. Des douleurs de la guerre va naître une chanson portée par Yves Montand, Les Feuilles mortes : un triomphe mondial.\nLe piano disparu continue pourtant de hanter les survivants...",
    "2026-08-27", 280, "9782221286807", 21.0),

    ("Nous aussi", 2, 5,
    "On fait partie d'une grande famille. On sait qu'on est privilégiés. On vit ensemble, dans notre immeuble au centre de Paris, on se retrouve l'été dans notre maison à la montagne. On trouve que c'est normal. C'est chez nous, c'est à nous, c'est pour nous. On se ressemble, on se compare, on se confronte, on ne se quitte pas, on se confond, on s'appartient. On ne sait pas comment dire je, on n'en a pas besoin, puisqu'on est nous. Nous les enfants, les frères et soeurs, les cousins, les cousines, on partage tout, nos écoles, nos chambres, nos habits, nos repas, nos jeux, nos bains, nos lits. On est les membres indissociables du grand corps familial. On n'a jamais vécu dehors. On ne sait pas ce que c'est. On n'en est pas capables. On n'en a même pas envie. Et tout aurait dû continuer ainsi, dans un même immuable recommencement. Le jour où la façade s'est fissurée, on n'a pas compris. Ça n'aurait pas dû se produire, pas dans notre famille. Ce n'était pas possible que ça nous arrive, à nous aussi.",
    "2026-08-29", 237, "9782330225575", 20.0),

    ("Joseph dans la nuit", 13, 6,
    "Voyageur épris d'ailleurs, de stop et de liberté, Olivier est en route vers Lahore pour fêter la nouvelle année sur une plage indienne. En traversant l'Iran, il est arrêté à Chiraz alors qu'explose le mouvement Femme, Vie, Liberté. Accusé d'espionnage, il reste deux ans et demi en prison.\nOlivier est un poète, habitué à vivre de peu, sans confort ni téléphone portable. En cellule, il mobilise tout ce qui peut lui apporter de la lumière, la poésie persane comme les chansons de Britney Spears.\nDerrière ses paupières, installé dans un cinéma dont il est le seul spectateur, il se projette des films. La nuit, il convoque dans ses rêves les êtres aimés.\nUn récit lumineux et bouleversant qui nous dit que, même dans la nuit, quelque chose en nous refusera toujours de céder. La découverte d'un écrivain.",
    "2026-08-20", 230, "9782378805975", 19.9),

    ("La solitude des professeurs est infinie", 3, 7,
    "Jean Deichel, jeune professeur de français, fait son stage dans un collège de la banlieue parisienne. La nuit, il loge dans un club de tennis à Deuil-la-Barre ; le jour, il découvre les difficultés du métier en même temps que ses joies profondes, la violence de l'École en même temps que sa beauté. \nJean est aussi un poète ivre d'aventure, attentif à trouver la lumière de la « vraie vie » au coeur du quotidien le plus gris : dans des jardins réels ou rêvés, au bord d'un lac, lors d'évasions à Pompéi et à Tarquinia, mais surtout dans la grâce fragile d'un cours réussi.\nEntre réalité politique et mystère existentiel, la vie des profs est un roman.",
    "2026-08-20", 313, "9782073161925", 21.5),

    ("JE", 4, 7,
    "« - Que savez-vous de la beauté, Antoinette ? Il se tourna vers moi, suspendu à ma réponse. - Pas grand-chose. Mais je sais la reconnaître quand elle est là. - Eh bien moi, chaque fois que je la vois, elle me blesse. Quand je vois votre visage, par exemple, quelque chose en moi se trouve comme ébranlé. »\nîle de la Jamaïque, 1831. Antoinette Cosway, créole de bonne famille, s'éprend d'Edward Rochester, un Anglais aussi impénétrable que fascinant. Mais à la séduction enflammée succèdent rapidement des scènes vénéneuses, où les baisers sont des blessures, où toute une société livre la jeune femme à son bourreau.\nDes années plus tard, Antoinette tente de conquérir sa propre histoire.\nJE se situe à mi-chemin entre roman victorien et thriller intimiste contemporain. Lilia Hassaine s'est inspirée du personnage de la première femme de Rochester dans Jane Eyre, le roman culte de Charlotte Brontë. Elle a choisi de lui donner une voix, un corps, une destinée.",
    "2026-08-20", 248, "9782073099945", 21.0),

    ("L'inconnue du quai de Javel", 1, 8, NULL, NULL, NULL, NULL, NULL),
    ("Une forêt", 12, 1, NULL, NULL, NULL, NULL, NULL),
    ("N'efface pas mes cercles", 14, 9, NULL, NULL, NULL, NULL, NULL),
    ("Choses que je croyais perdues", 10, 7, NULL, NULL, NULL, NULL, NULL),
    ("C'était ça ou mourir", 16, 3, NULL, NULL, NULL, NULL, NULL),
    ("De l'autre côté du lac", 9, 10, NULL, NULL, NULL, NULL, NULL),
    ("La guerre éternelle : souvenirs de Troie", 7, 7, NULL, NULL, NULL, NULL, NULL),
    ("Bataille au procès", 15, 11, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `go_main_character` (`mc_name`, `mc_id_book`) VALUES
    ("Minotaure", 1),
    ("narrator", 2),
    ("Madame", 3),
    ("Vieux Bouc", 3),
    ("Enfant timide", 3),
    ("narrator", 4),
    ("famille Enoch", 4),
    ("membres de la famille", 5),
    ("Olivier", 6),
    ("Jean Deichel", 7),
    ("Antoinette Cosway", 8),
    ("Edward Rochester", 8);

INSERT INTO `go_book_selection` (`bs_id_book`, `bs_id_selection`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1);


COMMIT;