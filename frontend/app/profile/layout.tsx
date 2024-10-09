import ProfileBar from "@components/ProfileBar/ProfileBar";

export default function ProfileLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div
      style={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <ProfileBar />
      {children}
    </div>
  );
}
