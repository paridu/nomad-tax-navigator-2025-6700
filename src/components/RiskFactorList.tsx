import { ComplianceFactor } from '@/types/compliance';
import { ShieldCheck, ShieldAlert, ChevronRight } from 'lucide-react';

export default function RiskFactorList({ factors }: { factors: ComplianceFactor[] }) {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-slate-100 overflow-hidden">
      <div className="p-6 border-b border-slate-50">
        <h3 className="font-bold text-slate-900">Compliance Audit Factors</h3>
      </div>
      <div className="divide-y divide-slate-50">
        {factors.map((factor, idx) => (
          <div key={idx} className="p-6 hover:bg-slate-50 transition-colors cursor-pointer group">
            <div className="flex items-start justify-between">
              <div className="flex gap-4">
                <div className={`mt-1 ${factor.score > 70 ? 'text-compass-emerald' : 'text-compass-gold'}`}>
                  {factor.score > 70 ? <ShieldCheck size={20} /> : <ShieldAlert size={20} />}
                </div>
                <div>
                  <h4 className="font-semibold text-slate-800">{factor.factor_name}</h4>
                  <p className="text-sm text-slate-500 mt-1">{factor.evidence}</p>
                  {factor.mitigation_advice && (
                    <p className="text-xs text-compass-slate mt-2 italic bg-slate-100 p-2 rounded">
                      Compass Advice: {factor.mitigation_advice}
                    </p>
                  )}
                </div>
              </div>
              <ChevronRight className="text-slate-300 group-hover:text-slate-500 transition-colors" size={20} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}