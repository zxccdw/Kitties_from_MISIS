import React from "react";
import styles from "./NavigationBar.module.scss";
import Image from "next/image";
import Logo from "../../assets/logos/Kokos_logo.png";
import Link from "next/link";
import SearchSvg from "../../assets/svg/search.svg";
import UserSvg from "../../assets/svg/user.svg";

type Props = {};

const NavigationBar = (props: Props) => {
  return (
    <div className={styles.nb_wrap}>
      <div className={styles.nb_wrap__nb}>
        <nav className={styles.nb_wrap__nb__sections}>
          <div className={styles.nb_wrap__nb__logo}>
            <Link href={"/"}>
              <Image src={Logo} alt="Logo" />
            </Link>
          </div>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/news"}
          >
            Новости
          </Link>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/matches"}
          >
            Матчи
          </Link>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/team"}
          >
            Команда
          </Link>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/shop"}
          >
            Магазин
          </Link>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/club"}
          >
            Клуб
          </Link>
          <Link
            className={styles.nb_wrap__nb__sections__section}
            href={"/contact"}
          >
            Контакты
          </Link>
        </nav>
        <div className={styles.nb_wrap__nb__lk}>
          <Image src={SearchSvg} alt="Search icon" />
          <Link href={"/login"}>
            <Image src={UserSvg} alt="User icon" />
          </Link>
        </div>
      </div>
    </div>
  );
};

export { NavigationBar };
