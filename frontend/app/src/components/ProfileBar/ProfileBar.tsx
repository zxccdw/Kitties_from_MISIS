import React from "react";
import styles from "./ProfileBar.module.scss";
import Link from "next/link";

type Props = {};

const ProfileBar = (props: Props) => {
  return (
    <nav className={styles.pb}>
      <Link href={"/profile"}>Мой профиль</Link>
      <Link href={"/profile/tickets"}>Мои билеты</Link>
      <Link href={"/profile/discussions"}>Мои обсуждения</Link>
      <Link href={"/profile/support"}>Поддержка</Link>
    </nav>
  );
};

export default ProfileBar;
