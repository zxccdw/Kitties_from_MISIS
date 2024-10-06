"use client";

import React, { useEffect, useState } from "react";
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import styles from "./page.module.css";

interface Event {
  id: number;
  date: Date;
  title: string;
}

const CalendarComponent: React.FC = () => {
  const [date, setDate] = useState<Date>(new Date());
  const [events, setEvents] = useState<Event[]>([]);
  const [eventName, setEventName] = useState<string>("");

  <div>
    <h3>События</h3>
    <ul>
      {events.map((event) => {
        return (
          <li>
            {event.date.getDate()} : {event.title}
          </li>
        );
      })}
    </ul>
  </div>;

  const handleAddEvent = (): void => {
    if (eventName && date) {
      const newEvent: Event = { id: Date.now(), date: date, title: eventName };
      setEvents([...events, newEvent]);
      setEventName("");
    }
  };

  const tileClassName = (date: Date): string | undefined => {
    if (
      events.some((event) => event.date.toDateString() === date.toDateString())
    ) {
      return styles.eventMarked;
    }
  };

  return (
    <div>
      <h2>Календарь мероприятий</h2>
      <Calendar
        onClickDay={(value) => {
          setDate(value);
          console.log(value);
        }}
        value={date}
        tileClassName={({ date }) => {
          return tileClassName(date);
        }}
      />
      <form onSubmit={(e): void => e.preventDefault()}>
        <input
          type="text"
          value={eventName}
          onChange={(e: React.ChangeEvent<HTMLInputElement>): void =>
            setEventName(e.target.value)
          }
          placeholder="Введите название мероприятия"
        />
        <button type="submit" onClick={handleAddEvent}>
          Добавить мероприятие
        </button>
      </form>
    </div>
  );
};

export { CalendarComponent };
