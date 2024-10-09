import { MatchCard } from "@/app/src/components/MatchCard/MatchCard";
import React from "react";
import styles from "./TicketsPage.module.scss";

type Props = {};

const TicketsPage = (props: Props) => {
  return (
    <div className={styles.tp}>
      <div className={styles.tp__card}>
        <MatchCard />
      </div>
    </div>
  );
};

export default TicketsPage;
