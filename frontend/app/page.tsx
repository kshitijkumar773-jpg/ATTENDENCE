import Link from "next/link";
import { ArrowUpRight, CalendarDays, ChevronDown, Clock3, LayoutDashboard, LogOut, MoreHorizontal, ScanFace, Settings, ShieldCheck, UserPlus, Users } from "lucide-react";

const rows = [
  ["Aarav Sharma", "ST-2048", "09:02 AM", "Present", "AS", "mint"],
  ["Ananya Mehta", "ST-2037", "09:04 AM", "Present", "AM", "coral"],
  ["Vihaan Kapoor", "ST-2051", "09:11 AM", "Late", "VK", "gold"],
  ["Diya Nair", "ST-2019", "09:18 AM", "Present", "DN", "lavender"],
];

export default function HomePage() {
  return <main className="app-shell">
    <aside className="sidebar">
      <div className="brand-lockup"><div className="brand-mark"><ScanFace size={22} /></div><div><strong>ClassVision</strong><span>Attendance OS</span></div></div>
      <div className="workspace-label">Workspace</div>
      <nav className="side-nav"><Link className="nav-item active" href="/"><LayoutDashboard size={18} /> Overview</Link><Link className="nav-item" href="/teacher/dashboard"><CalendarDays size={18} /> Attendance</Link><Link className="nav-item" href="/student/registrationform"><UserPlus size={18} /> Students</Link><Link className="nav-item" href="/teacher/start-session"><ScanFace size={18} /> Live session</Link></nav>
      <div className="workspace-label settings-label">Manage</div><nav className="side-nav"><Link className="nav-item" href="/teacher/updatedetails"><Settings size={18} /> Settings</Link></nav>
      <div className="sidebar-bottom"><div className="security-note"><ShieldCheck size={18} /><span><b>Privacy first</b><small>Face data stays protected</small></span></div><button className="logout-button" type="button"><LogOut size={17} /> Sign out</button></div>
    </aside>
    <section className="main-panel">
      <header className="topbar"><div className="breadcrumb"><span>Workspace</span><b>/</b><strong>Overview</strong></div><div className="profile-menu"><div className="profile-avatar">RK</div><span><b>Rahul Kumar</b><small>Administrator</small></span><ChevronDown size={16} /></div></header>
      <div className="page-content">
        <section className="welcome-row"><div><p className="eyebrow">THURSDAY, 10 SEPTEMBER 2026</p><h1>Good morning, Rahul.</h1><p className="subheading">Here&apos;s what&apos;s happening across your classroom today.</p></div><Link className="primary-button" href="/teacher/start-session"><ScanFace size={18} /> Start live session <ArrowUpRight size={16} /></Link></section>
        <section className="stats-grid"><Stat icon={<Users size={20} />} label="Students enrolled" value="248" trend="+12%" note="this month" /><Stat icon={<ScanFace size={20} />} label="Present today" value="214" trend="86.3%" note="attendance rate" tone="blue" /><Stat icon={<Clock3 size={20} />} label="Late arrivals" value="09" trend="-3" note="from yesterday" tone="yellow" /><Stat icon={<CalendarDays size={20} />} label="Sessions this week" value="18" trend="+4" note="from last week" tone="pink" /></section>
        <section className="content-grid">
          <article className="panel attendance-panel"><PanelHeading title="Today&apos;s attendance" subtitle="Live overview of your latest session" /><div className="session-banner"><div className="live-pulse"><span /> Live session</div><strong>Computer Science · Grade 10A</strong><span className="session-time"><Clock3 size={14} /> 08:45 – 10:00 AM</span></div><div className="table-wrap"><table><thead><tr><th>Student</th><th>Check-in time</th><th>Status</th><th /></tr></thead><tbody>{rows.map(([name, id, time, status, initials, color]) => <tr key={id}><td><div className="student-cell"><span className={`student-avatar ${color}`}>{initials}</span><span><b>{name}</b><small>{id}</small></span></div></td><td>{time}</td><td><span className={`status ${status.toLowerCase()}`}>{status}</span></td><td><button className="row-menu" aria-label={`Options for ${name}`} type="button"><MoreHorizontal size={17} /></button></td></tr>)}</tbody></table></div><Link className="panel-link" href="/teacher/dashboard">View complete attendance <ArrowUpRight size={15} /></Link></article>
          <article className="panel quick-panel"><PanelHeading title="Quick actions" subtitle="Common tasks, right where you need them" /><div className="quick-actions"><QuickAction href="/student/registrationform" icon={<UserPlus size={19} />} title="Register student" note="Add a new face profile" tone="green" /><QuickAction href="/teacher/start-session" icon={<ScanFace size={19} />} title="Start attendance" note="Open camera session" tone="violet" /><QuickAction href="/teacher/dashboard" icon={<CalendarDays size={19} />} title="Export report" note="Download class records" tone="orange" /></div><div className="tip-box"><span>✦</span><p><b>Tip for better accuracy</b><br />Make sure the room has even lighting before starting a session.</p></div></article>
        </section>
      </div>
    </section>
  </main>;
}

function Stat({ icon, label, value, trend, note, tone = "green" }: { icon: React.ReactNode; label: string; value: string; trend: string; note: string; tone?: string }) { return <article className={`stat-card ${tone === "green" ? "accent-card" : ""}`}><div className={`stat-icon ${tone}-icon`}>{icon}</div><p>{label}</p><strong>{value}</strong><span className={`stat-trend ${tone === "yellow" ? "neutral" : "positive"}`}>{trend} <em>{note}</em></span></article>; }
function PanelHeading({ title, subtitle }: { title: string; subtitle: string }) { return <div className="panel-heading"><div><h2>{title}</h2><p>{subtitle}</p></div><button className="icon-button" aria-label="More options" type="button"><MoreHorizontal size={20} /></button></div>; }
function QuickAction({ href, icon, title, note, tone }: { href: string; icon: React.ReactNode; title: string; note: string; tone: string }) { return <Link href={href} className="quick-action"><span className={`quick-icon ${tone}-icon`}>{icon}</span><span><b>{title}</b><small>{note}</small></span><ArrowUpRight size={16} /></Link>; }