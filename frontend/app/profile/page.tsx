import React from "react";
import { Profile } from "./model";
import styles from "./ProfilePage.module.scss";
import Image from "next/image";
import { ProfileDescriptionTextArea } from "../src/components/ProfileDescriptionTextArea/ProfileDescriptionTextArea";

type Props = {};

const ProfilePage = (props: Props) => {
  return (
    <div className={styles.pp}>
      <div className={styles.pp__profilePhoto}>
        <Image src={""} alt="Фото профиля"></Image>
      </div>
      <div className={styles.pp__rest}>
        <div className={styles.pp__rest__head}>
          <div className={styles.pp__rest_head__data}>
            <div className={styles.pp__rest__head__data__name}>Александр</div>
            <div className={styles.pp__rest__head__data__surname}>Гребенюк</div>
          </div>
          <button>
            <Image src={""} alt="Иконка редактирования профиля" />
          </button>
          <div>
            <Image src={""} alt="Значок статуса фаната" />
          </div>
        </div>
        <div className={styles.pp__rest__textarea}>
          <ProfileDescriptionTextArea />
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
