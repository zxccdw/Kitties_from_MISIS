import { PostCardProps } from "@/app/page";
import styles from "./PostCard.module.scss";
import Image from "next/image";

export const PostCard = ({
  imgSrc,
  title,
  description,
  date = "",
}: PostCardProps): JSX.Element => {
  return (
    <div className={styles.item}>
      <div className={styles.blockPhoto}>
        <Image src={imgSrc} alt="No photo" className={styles.photoCard} />
      </div>
      <div className={styles.description}>
        <div className={styles.descriptionTitle}>
          <p className={styles.descriptionTitle__text}>{title}</p>
        </div>
        <div className={styles.descriptionText}>
          <p className={styles.descriptionText__text}>{description}</p>
        </div>
        <div className={styles.descriptionDate}>
          <div className={styles.date}>{date}</div>
        </div>
      </div>
    </div>
  );
};
