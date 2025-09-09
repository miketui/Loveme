import React from 'react';

const ChapterTitlePageMockup = () => {
  const mockChapterData = {
    roman: "VI",
    titleLines: [
      "MASTERING",
      "THE", 
      "BUSINESS",
      "OF",
      "HAIRSTYLING"
    ],
    bibleQuote: {
      text: "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.",
      ref: "— Colossians 3:23"
    },
    introText: "Picture this powerful scene: You stand poised behind your styling chair, ready to transform a simple canvas of hair into a masterpiece. As you begin to weave your magic, a sudden thought invades—are your business skills as sharp as the tools in your hands? In the fast-paced world of hairstyling, where artistry and entrepreneurship dance an intricate duet, mastering the business side is as essential as perfecting your hands-on craft."
  };

  return (
    <div className="w-full max-w-4xl mx-auto bg-white p-8 shadow-lg" style={{ fontFamily: 'Georgia, serif', minHeight: '100vh' }}>
      
      {/* Header showing this is ACISS Design System Template */}
      <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mb-8">
        <h3 className="text-lg font-bold text-blue-800 mb-2">ACISS Design System - Chapter Title Page Template</h3>
        <p className="text-blue-700 text-sm">
          This visual mockup demonstrates the exact layout and styling requirements for all 16 chapter files. 
          Every chapter must follow this precise structure while preserving 100% of the original content.
        </p>
      </div>

      {/* Chapter Number with Brushstroke Background */}
      <div className="flex justify-center mb-8">
        <div className="relative">
          {/* Brushstroke background simulation */}
          <div 
            className="w-32 h-20 flex items-center justify-center rounded-full relative"
            style={{
              background: 'linear-gradient(135deg, #8B4513, #D2691E, #CD853F)',
              backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='128' height='80' viewBox='0 0 128 80'%3E%3Cpath d='M15,40 Q35,15 65,35 Q95,55 115,40 Q105,25 85,30 Q65,35 45,25 Q25,15 15,40 Z' fill='%23654321' opacity='0.4'/%3E%3C/svg%3E")`,
              boxShadow: '0 6px 20px rgba(139, 69, 19, 0.4)',
              border: '2px solid rgba(101, 67, 33, 0.3)'
            }}
          >
            <span 
              className="text-white font-bold text-4xl relative z-10"
              style={{ 
                fontFamily: '"Cinzel Decorative", Georgia, serif',
                textShadow: '3px 3px 6px rgba(0,0,0,0.7)',
                letterSpacing: '3px'
              }}
            >
              {mockChapterData.roman}
            </span>
          </div>
          <div className="text-xs text-center mt-2 text-gray-600 italic">
            CSS: .chapter-number-brush + brushstroke.JPEG
          </div>
        </div>
      </div>

      {/* Title Stack with Vertical Bar */}
      <div className="flex items-start gap-6 mb-8 justify-start">
        {/* Vertical accent bar */}
        <div 
          className="w-2 bg-teal-600 flex-shrink-0 rounded-full"
          style={{ height: '320px', backgroundColor: '#1797a6', boxShadow: '0 2px 8px rgba(23, 151, 166, 0.3)' }}
        >
          <div className="text-xs text-gray-600 italic mt-2 ml-3 transform rotate-90 origin-left whitespace-nowrap">
            CSS: .title-bar
          </div>
        </div>
        
        {/* Stacked title lines */}
        <div className="flex flex-col gap-1">
          {mockChapterData.titleLines.map((line, index) => (
            <h1 
              key={index}
              className="text-left font-bold leading-tight"
              style={{
                fontFamily: '"Cinzel Decorative", Georgia, serif',
                fontSize: '2.4rem',
                color: '#1797a6',
                textTransform: 'uppercase',
                letterSpacing: '0.05em',
                margin: 0,
                textShadow: '1px 1px 2px rgba(0,0,0,0.1)'
              }}
            >
              {line}
            </h1>
          ))}
          <div className="text-xs text-gray-600 italic mt-2">
            CSS: .title-stack → .title-line (each line)
          </div>
        </div>
      </div>

      {/* Bible Quote Container */}
      <div className="flex justify-center mb-8">
        <div 
          className="max-w-2xl text-center px-8 py-6 rounded-2xl border-2 relative"
          style={{
            backgroundColor: '#e0f7fa',
            borderColor: '#1797a6',
            boxShadow: '0 4px 16px rgba(23, 151, 166, 0.2)',
            borderRadius: '50px'
          }}
        >
          <blockquote 
            className="text-lg mb-3"
            style={{ 
              fontFamily: 'Georgia, serif',
              fontStyle: 'italic',
              color: '#333',
              lineHeight: '1.6'
            }}
          >
            "{mockChapterData.bibleQuote.text}"
          </blockquote>
          <cite 
            className="text-base font-medium"
            style={{ 
              color: '#1797a6',
              fontFamily: 'Georgia, serif',
              fontStyle: 'italic'
            }}
          >
            {mockChapterData.bibleQuote.ref}
          </cite>
          <div className="text-xs text-gray-600 italic mt-3">
            CSS: .bible-quote-container (pill shape)
          </div>
        </div>
      </div>

      {/* Introduction Heading */}
      <div className="text-center mb-6">
        <h2 
          className="font-bold tracking-wider relative inline-block"
          style={{
            fontFamily: '"Montserrat", Arial, sans-serif',
            fontSize: '1.2rem',
            color: '#555',
            textTransform: 'uppercase',
            letterSpacing: '0.1em'
          }}
        >
          Introduction
          <div className="absolute -bottom-1 left-0 right-0 h-0.5 bg-teal-600 opacity-30"></div>
        </h2>
        <div className="text-xs text-gray-600 italic mt-2">
          CSS: .introduction-heading
        </div>
      </div>

      {/* Introduction Paragraph with Dropcap */}
      <div className="max-w-4xl mx-auto relative">
        <p 
          className="text-justify leading-relaxed"
          style={{ 
            fontFamily: 'Georgia, serif',
            fontSize: '1.15rem',
            lineHeight: '1.8',
            color: '#1a1a1a'
          }}
        >
          <span 
            className="float-left font-bold mr-3 mt-1 relative"
            style={{
              fontFamily: '"Cinzel Decorative", Georgia, serif',
              fontSize: '4rem',
              lineHeight: '1',
              color: '#ffffff',
              backgroundColor: '#1797a6',
              padding: '0.1em 0.35em 0.2em 0.35em',
              borderRadius: '8px',
              boxShadow: '0 3px 12px rgba(23, 151, 166, 0.4)',
              border: '2px solid rgba(255, 255, 255, 0.9)'
            }}
          >
            P
          </span>
          {mockChapterData.introText}
        </p>
        <div className="text-xs text-gray-600 italic mt-4 clear-both">
          CSS: .dropcap-first-letter (first letter with accent background)
        </div>
      </div>

      {/* Design System Notes */}
      <div className="mt-16 p-6 bg-gray-50 border-2 border-gray-200 rounded-lg">
        <h3 className="text-lg font-bold text-gray-800 mb-4">ACISS Design System Requirements</h3>
        
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-gray-700 mb-2">Visual Elements:</h4>
            <ul className="text-sm text-gray-600 space-y-1">
              <li>• Roman numeral with brushstroke background (TOP CENTERED)</li>
              <li>• Vertical title stack with accent bar (left-aligned)</li>
              <li>• Bible quote in pill-shaped container (centered)</li>
              <li>• Introduction heading with underline (centered)</li>
              <li>• Dropcap first letter with accent background</li>
            </ul>
          </div>
          
          <div>
            <h4 className="font-semibold text-gray-700 mb-2">Content Requirements:</h4>
            <ul className="text-sm text-gray-600 space-y-1">
              <li>• 100% content preservation (every word)</li>
              <li>• All footnotes and references maintained</li>
              <li>• Case studies and examples kept intact</li>
              <li>• Personal stories preserved word-for-word</li>
              <li>• Implementation steps maintained exactly</li>
            </ul>
          </div>
        </div>

        <div className="mt-4 p-4 bg-yellow-50 border-l-4 border-yellow-400">
          <p className="text-sm text-yellow-800">
            <strong>Critical:</strong> This visual structure must be applied to all 16 chapter files while preserving 
            every single word from the original content. No truncation, summarization, or content changes allowed.
          </p>
        </div>
      </div>

      {/* Page Structure Indicator */}
      <div className="mt-8 text-center">
        <div className="inline-flex items-center space-x-2 text-sm text-gray-600">
          <div className="w-3 h-3 bg-teal-600 rounded-full"></div>
          <span>Page 1 of 6</span>
          <div className="text-xs italic">(Title Page → Body Content → Endnotes → Quiz & Worksheet)</div>
        </div>
      </div>
    </div>
  );
};

export default ChapterTitlePageMockup;