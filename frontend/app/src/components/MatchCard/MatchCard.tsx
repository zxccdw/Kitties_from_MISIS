import React from "react";
import styles from "./MatchCard.module.scss";

type Props = {};

const MatchCard = (props: Props) => {
  return (
    <div className={styles.mc} style={{ borderLeft: "13px solid red" }}>
      <span>Кокос Групп</span>
      <span>против</span>
      <span>Команда инвалидов</span>

      <div className={styles.mc__data}>
        <span>№123456789</span>
        <span>12 октября</span>
        <span>19:00</span>
      </div>
    </div>
  );
};

export { MatchCard };
