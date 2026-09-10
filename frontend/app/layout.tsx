import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Face Recognition System",
  description: "Full-stack Flask + Next.js Face Recognition App",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        {children}
        
      </body>
    </html>
  );
}
