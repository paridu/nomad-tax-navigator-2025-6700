import ComplianceGauge from '@/components/ComplianceGauge';
import LocationCard from '@/components/LocationCard';
import RiskFactorList from '@/components/RiskFactorList';
import { ComplianceReport } from '@/types/compliance';
import { LayoutDashboard, Globe, FileText, Settings, Bell } from 'lucide-react';

// Mock Data (In production, this comes from FastAPI backend)
const mockReport: ComplianceReport = {
  user_id: "user_123",
  country_code: "TH",
  country_name: "Thailand",
  overall_compliance_score: 82,
  risk_level: "LOW",
  days_spent: 45,
  tax_threshold_days: 180,
  dta_applied: true,
  interpretation_summary: "Your status is protected under the Thai-German DTA Article 4.",
  factors: [
    {
      factor_name: "Physical Presence",
      weight: 0.4,
      score: 95,
      evidence: "45/180 days utilized. No residency risk until 135 more days.",
    },
    {
      factor_name: "Permanent Establishment",
      weight: 0.3,
      score: 65,
      evidence: "Working from a dedicated co-working space might trigger fixed place of business.",
      mitigation_advice: "Vary your work locations to avoid 'Fixed Place' interpretation."
    }
  ],
  next_steps: [
    "Log your next border crossing",
    "Download DTA Residency Certificate",
    "Review PE risk for Q3"
  ]
};

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-[#F8FAFC] flex">
      {/* Sidebar - Desktop */}
      <aside className="w-64 bg-compass-navy hidden lg:flex flex-col p-6 text-white">
        <div className="mb-10">
          <h1 className="text-xl font-bold tracking-tighter flex items-center gap-2">
            <Globe className="text-compass-gold" />
            COMPASS
          </h1>
        </div>
        <nav className="space-y-2 flex-1">
          <a href="#" className="flex items-center gap-3 p-3 bg-white/10 rounded-xl text-sm font-medium">
            <LayoutDashboard size={18} /> Dashboard
          </a>
          <a href="#" className="flex items-center gap-3 p-3 text-white/60 hover:text-white transition-colors text-sm font-medium">
            <Globe size={18} /> Global Strategy
          </a>
          <a href="#" className="flex items-center gap-3 p-3 text-white/60 hover:text-white transition-colors text-sm font-medium">
            <FileText size={18} /> Documents
          </a>
        </nav>
        <div className="mt-auto pt-6 border-t border-white/10">
          <a href="#" className="flex items-center gap-3 p-3 text-white/60 text-sm font-medium">
            <Settings size={18} /> Settings
          </a>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-4 md:p-8 lg:p-12 max-w-7xl mx-auto w-full">
        {/* Header */}
        <header className="flex justify-between items-center mb-8">
          <div>
            <h2 className="text-2xl font-bold text-slate-900">Welcome back, Nomad</h2>
            <p className="text-slate-500">Your global compliance status is looking stable.</p>
          </div>
          <button className="relative p-2 text-slate-400 hover:text-slate-600 transition-colors">
            <Bell size={24} />
            <span className="absolute top-2 right-2 w-2 h-2 bg-compass-rose rounded-full" />
          </button>
        </header>

        {/* Top Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex flex-col items-center">
            <h3 className="text-sm font-medium text-slate-500 mb-2">Overall Score</h3>
            <ComplianceGauge score={mockReport.overall_compliance_score} riskLevel={mockReport.risk_level} />
          </div>

          <LocationCard 
            countryName={mockReport.country_name} 
            daysSpent={mockReport.days_spent} 
            threshold={mockReport.tax_threshold_days} 
          />

          <div className="bg-compass-navy rounded-2xl p-6 shadow-lg text-white">
            <h3 className="font-bold mb-4">Immediate Next Steps</h3>
            <ul className="space-y-4">
              {mockReport.next_steps.map((step, i) => (
                <li key={i} className="flex items-center gap-3 text-sm text-white/80">
                  <div className="w-5 h-5 rounded-full bg-compass-gold/20 flex items-center justify-center text-compass-gold font-bold text-[10px]">
                    {i + 1}
                  </div>
                  {step}
                </li>
              ))}
            </ul>
            <button className="w-full mt-6 py-3 bg-compass-gold text-compass-navy font-bold rounded-xl text-sm hover:brightness-110 transition-all">
              Execute Actions
            </button>
          </div>
        </div>

        {/* Detailed Factors */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <RiskFactorList factors={mockReport.factors} />
          </div>
          <div className="space-y-6">
            <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
              <h4 className="font-bold text-slate-900 mb-2">DTA Analysis</h4>
              <p className="text-sm text-slate-600 leading-relaxed">
                {mockReport.interpretation_summary}
              </p>
              <div className="mt-4 pt-4 border-t border-slate-50">
                <span className="inline-flex items-center gap-1 text-xs font-bold text-compass-emerald">
                  <ShieldCheck size={14} /> TREATY PROTECTED
                </span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}