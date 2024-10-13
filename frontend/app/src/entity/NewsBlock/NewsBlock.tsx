import Image, { StaticImageData } from "next/image";
import arrowLeft from "../../assets/png/ArrowLeft.png";
import arrowRight from "../../assets/png/ArrowRight.png";
import styles from "./NewsBlock.module.scss";
import { PostCard } from "../PostCard/PostCard";
import backgroundCard from "../../assets/background/loadingImage.png";

interface newsBlockProps {
  btnName: string;
  titleBlock: string;
}

export const NewsBlock = ({ btnName, titleBlock }: newsBlockProps) => {
  return (
    <div className={styles.page__newsBlock}>
      <p className={styles.page__newsBlockTitle}>{titleBlock}</p>
      <div className={styles.page__newsBlockPost}>
        <div>
          <Image
            alt="Arrow Left"
            src={arrowLeft}
            className={styles.page__newsArrow}
          />
        </div>
        <div style={{ width: "25%", height: "80%" }}>
          <PostCard
            title="Заголовок"
            description="Краткое описание"
            imgSrc={backgroundCard}
          />
        </div>
        <div style={{ width: "25%", height: "80%" }}>
          <PostCard
            title="Заголовок"
            description="Краткое описание"
            imgSrc={backgroundCard}
          />
        </div>
        <div style={{ width: "25%", height: "80%" }}>
          <PostCard
            title="Заголовок"
            description="Краткое описание"
            imgSrc={backgroundCard}
          />
        </div>
        <div>
          <Image
            alt="Arrow Right"
            src={arrowRight}
            className={styles.page__newsArrow}
          />
        </div>
      </div>
      <div className={styles.page__newsMoreButton}>
        <button>{btnName}</button>
      </div>
    </div>
  );
};
