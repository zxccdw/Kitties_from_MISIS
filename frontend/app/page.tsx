import Image from "next/image";
import styles from "./page.module.scss";
import stadium from "./src/assets/background/stadium.png";
import backgroundCard from "./src/assets/background/loadingImage.png";
import { styleText } from "util";

export default function Home() {
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
        <div
          style={{
            position: "absolute",
            top: "100px",
            alignItems: "center",
            justifyContent: "center",
            display: "flex",
            flexDirection: "column",
            rowGap: "20px",
          }}
        >
          <h1 style={{ fontSize: "72px", color: "white" }}>ВМЕСТЕ К ПОБЕДЕ!</h1>
          <button
            style={{
              width: "45%",
              paddingTop: "10px",
              paddingBottom: "10px",
              fontSize: "24px",
              borderRadius: "20px",
              border: "none",
              color: "white",
              backgroundColor: "#E02A26",
            }}
          >
            ПРИСОЕДИНЯЙСЯ К НАМ!
          </button>
        </div>
        <div className={styles.page__actualList}>
          <div className={styles.actualList}>
            <div className={styles.actualList__item}>
              <div className={styles.actualList__blockPhoto}>
                <Image
                  src={backgroundCard}
                  alt="No photo"
                  className={styles.actualList__photoCard}
                />
              </div>
              <div className={styles.actualList__description}>
                <div className={styles.actualList__descriptionTitle}>
                  <p className={styles.actualList__descriptionTitle__text}>
                    Победа!
                  </p>
                </div>
                <div className={styles.actualList__descriptionText}>
                  <p className={styles.actualList__descriptionText__text}>
                    2:0 в пользу ФК Кокос групп
                  </p>
                </div>
                <div className={styles.actualList__descriptionDate}>
                  <time
                    dateTime="2024-10-03"
                    className={styles.actualList__date}
                  >
                    03.10.2024
                  </time>
                </div>
              </div>
            </div>
            <div className={styles.actualList__item}>
              <div className={styles.actualList__blockPhoto}>
                <Image
                  src={backgroundCard}
                  alt="No photo"
                  className={styles.actualList__photoCard}
                />
              </div>
              <div className={styles.actualList__description}>
                <div className={styles.actualList__descriptionTitle}>
                  <p className={styles.actualList__descriptionTitle__text}>
                    Предстоящий матч
                  </p>
                </div>
                <div className={styles.actualList__descriptionText}>
                  <p className={styles.actualList__descriptionText__text}>
                    Не пропустите
                  </p>
                </div>
                <div className={styles.actualList__descriptionDate}>
                  <time
                    dateTime="2024-10-03"
                    className={styles.actualList__date}
                  >
                    12.10.2024
                  </time>
                </div>
              </div>
            </div>
            <div className={styles.actualList__item}>
              <div className={styles.actualList__blockPhoto}>
                <Image
                  src={backgroundCard}
                  alt="No photo"
                  className={styles.actualList__photoCard}
                />
              </div>
              <div className={styles.actualList__description}>
                <div className={styles.actualList__descriptionTitle}>
                  <p className={styles.actualList__descriptionTitle__text}>
                    Интервью с капитаном
                  </p>
                </div>
                <div className={styles.actualList__descriptionText}>
                  <p className={styles.actualList__descriptionText__text}>
                    Краткое описание
                  </p>
                </div>
                <div className={styles.actualList__descriptionDate}>
                  <time
                    dateTime="2024-10-03"
                    className={styles.actualList__date}
                  >
                    16.10.2024
                  </time>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
