START TRANSACTION;

DROP TABLE IF EXISTS `go_book_selection`, `go_main_character`, `go_selection`, `go_jury`, `go_book`, `go_author`;

CREATE TABLE IF NOT EXISTS `go_author` (
    `au_id_author` INT NOT NULL AUTO_INCREMENT,
    `au_first_name` VARCHAR(50) NOT NULL,
    `au_last_name` VARCHAR(50) NOT NULL,
    `au_biography` TEXT NOT NULL,
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

CREATE TABLE IF NOT EXISTS `go_book` (
    `bo_id_book` INT NOT NULL AUTO_INCREMENT,
    `bo_title` VARCHAR(100) NOT NULL,
    `bo_summary` text NOT NULL,
    `bo_publication_date` DATE NOT NULL,
    `bo_number_of_pages` INT NOT NULL,
    `bo_isbn` INT NOT NULL,
    `bo_price` DECIMAL(10,2) NOT NULL,
    `bo_id_author` INT NOT NULL,
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
    ON DELETE CASCADE;

ALTER TABLE `go_main_character`
    ADD CONSTRAINT `go_main_character_fk1` FOREIGN KEY (`mc_id_book`) REFERENCES `go_book` (`bo_id_book`)
    ON DELETE CASCADE;

ALTER TABLE `go_book_selection`
    ADD CONSTRAINT `go_book_selection_fk1` FOREIGN KEY (`bs_id_book`) REFERENCES `go_book` (`bo_id_book`)
    ON DELETE CASCADE,
    ADD CONSTRAINT `go_book_selection_fk2` FOREIGN KEY (`bs_id_selection`) REFERENCES `go_selection` (`se_id_selection`)
    ON DELETE CASCADE;

COMMIT;