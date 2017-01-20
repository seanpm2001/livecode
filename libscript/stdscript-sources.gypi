{
	'variables':
	{
		# Source LCB files for the stdscript library containing syntax
		'stdscript_syntax_lcb_files':
		[
			'src/arithmetic.lcb',
			'src/array.lcb',
			'src/assert.lcb',
			'src/binary.lcb',
			'src/bitwise.lcb',
			'src/byte.lcb',
			'src/char.lcb',
			'src/codeunit.lcb',
			'src/date.lcb',
			#'src/encoding.lcb',
			'src/file.lcb',
			'src/foreign.lcb',
			#'src/item.lcb',
			#'src/line.lcb',
			'src/list.lcb',
			'src/logic.lcb',
			#'src/map.lcb',
			'src/math.lcb',
			'src/math-foundation.lcb',
			#'src/segmentchunk.lcb',
			'src/sort.lcb',
			'src/stream.lcb',
			'src/string.lcb',
			'src/system.lcb',
			'src/type.lcb',
			'src/type-convert.lcb',
			'src/unittest.lcb',
			#'src/url.lcb',
		],
		
		'stdscript_other_lcb_files':
		[
			'src/unittest-impl.lcb',
		],
		
		'stdscript_sources':
		[
			'src/module-arithmetic.cpp',
			'src/module-array.cpp',
			'src/module-assert.cpp',
			'src/module-binary.cpp',
			'src/module-bitwise.cpp',
			'src/module-byte.cpp',
			'src/module-char.cpp',
			'src/module-codeunit.cpp',
			'src/module-date.cpp',
			'src/module-encoding.cpp',
			'src/module-file.cpp',
			'src/module-foreign.cpp',
			'src/module-list.cpp',
			'src/module-logic.cpp',
			'src/module-map.cpp',
			'src/module-math_foundation.cpp',
			'src/module-math.cpp',
			'src/module-sort.cpp',
			'src/module-stream.cpp',
			'src/module-string.cpp',
			'src/module-system.cpp',
			'src/module-type_convert.cpp',
			'src/module-type.cpp',
			'src/module-unittest.cpp',
			'src/module-unittest_IMPL.cpp',
			'src/module-url.cpp',
		],
	},
}
