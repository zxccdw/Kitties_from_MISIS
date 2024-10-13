"use client";

import Image, { StaticImageData } from "next/image";
import styles from "./page.module.scss";
import stadium from "./src/assets/background/stadium.png";
import backgroundCard from "./src/assets/background/loadingImage.png";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { PostCard } from "./src/entity/PostCard/PostCard";
import { NewsBlock } from "./src/entity/NewsBlock/NewsBlock";
import arrowLeft from "./src/assets/background/nophoto.jpg";

export interface PostCardProps {
  imgSrc: StaticImageData;
  title: string;
  description: string;
  date?: string;
}

export default function Home() {
  const [news, setNews] = useState<PostCardProps[]>([
    {
      imgSrc: backgroundCard,
      title: "Победа!",
      description: "2:0 в пользу ФК Кокос групп",
      date: "03.10.2024",
    },
    {
      imgSrc: backgroundCard,
      title: "Предстоящий матч",
      description: "Не пропустите",
      date: "12.10.2024",
    },
    {
      imgSrc: backgroundCard,
      title: "Интервью с капитаном",
      description: "Краткое описание",
      date: "16.10.2024",
    },
  ]);

  const router = useRouter();

  return (
    <div className={styles.page}>
      <div className={styles.page__welcBlock}>
        <div className={styles.page__stadium}>
          <Image
            src={stadium}
            alt="Stadium"
            className={styles.page__backgroundStaduimImage}
          />
        </div>
        <div className={styles.page__joinBlock}>
          <h1 className={styles.page__joinBlockText}>ВМЕСТЕ К ПОБЕДЕ!</h1>
          <button
            className={styles.page__joinBlockButton}
            onClick={() => router.push("/LogStart")}
          >
            ПРИСОЕДИНЯЙСЯ К НАМ!
          </button>
        </div>
        <div className={styles.actualList}>
          {news.map((element, index) => (
            <div key={index} className={styles.actualList__blockCard}>
              <PostCard
                imgSrc={element.imgSrc}
                title={element.title}
                description={element.description}
                date={element.date}
              />
            </div>
          ))}
        </div>
      </div>
      <NewsBlock btnName="ЕЩЕ НОВОСТИ" titleBlock="Новости" />
      <NewsBlock btnName="ВСЯ КОМАНДА" titleBlock="Команда" />
      <div className={styles.shopBlockBack}>
        <div className={styles.shopBlock}>
          <div className={styles.shopBlock__content}>
            <div className={styles.shopBlock__title}>
              <p>Магазин</p>
            </div>
            <div className={styles.shopBlock__title2}>
              <p>Приобретай прямо сейчас!</p>
            </div>
            <div className={styles.shopBlock__card}>
              <div>
                <Image src={arrowLeft} alt="arrow left" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
