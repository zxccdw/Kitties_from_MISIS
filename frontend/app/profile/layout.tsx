import ProfileBar from "@components/ProfileBar/ProfileBar";

export default function ProfileLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div>
      <ProfileBar />
      {children}
    </div>
  );
}
