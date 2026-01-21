import { MapPin, Calendar, AlertCircle } from 'lucide-react';

interface Props {
  countryName: string;
  daysSpent: number;
  threshold: number;
}

export default function LocationCard({ countryName, daysSpent, threshold }: Props) {
  const percentage = (daysSpent / threshold) * 100;
  const isWarning = percentage > 80;

  return (
    <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
      <div className="flex justify-between items-start mb-4">
        <div>
          <p className="text-sm font-medium text-slate-500">Current Location</p>
          <h3 className="text-2xl font-bold flex items-center gap-2 text-slate-900">
            <MapPin className="text-compass-gold" size={24} />
            {countryName}
          </h3>
        </div>
        <div className="bg-compass-navy text-white px-3 py-1 rounded-full text-xs font-bold">
          LIVE
        </div>
      </div>

      <div className="space-y-4">
        <div className="flex justify-between text-sm">
          <span className="text-slate-600">Tax Residency Clock</span>
          <span className="font-mono font-bold">
            {daysSpent} / {threshold} Days
          </span>
        </div>
        
        <div className="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
          <div 
            className={`h-full transition-all duration-500 ${isWarning ? 'bg-compass-rose' : 'bg-compass-emerald'}`}
            style={{ width: `${Math.min(percentage, 100)}%` }}
          />
        </div>

        {isWarning && (
          <div className="flex items-center gap-2 p-3 bg-rose-50 border border-rose-100 rounded-lg text-rose-700 text-sm">
            <AlertCircle size={16} />
            <span>Approaching tax residency trigger point.</span>
          </div>
        )}
      </div>
    </div>
  );
}