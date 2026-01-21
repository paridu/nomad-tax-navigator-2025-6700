'use client';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

interface Props {
  score: number;
  riskLevel: string;
}

export default function ComplianceGauge({ score, riskLevel }: Props) {
  const data = [
    { value: score },
    { value: 100 - score },
  ];

  const getColor = (level: string) => {
    switch (level) {
      case 'LOW': return '#10B981';
      case 'MEDIUM': return '#F59E0B';
      case 'HIGH': return '#F43F5E';
      default: return '#94A3B8';
    }
  };

  return (
    <div className="relative h-48 w-48 mx-auto">
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            innerRadius={60}
            outerRadius={80}
            startAngle={180}
            endAngle={0}
            paddingAngle={0}
            dataKey="value"
          >
            <Cell fill={getColor(riskLevel)} />
            <Cell fill="#E2E8F0" />
          </Pie>
        </PieChart>
      </ResponsiveContainer>
      <div className="absolute inset-0 flex flex-col items-center justify-center pt-8">
        <span className="text-3xl font-bold text-slate-900">{score}%</span>
        <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
          {riskLevel} RISK
        </span>
      </div>
    </div>
  );
}